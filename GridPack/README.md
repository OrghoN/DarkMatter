`/afs/cern.ch/work/a/abdollah/scratch1/GenStudy/CMSSW_7_1_21_patch1/src/genproductions/bin/MadGraph5_aMCatNLO`

## Steps to make GridPack "now for Dark Matter in Coannihilation" signal

1. Need to have a model Now the model is already uploaded "DarkMatter_Codex.zip":
`/afs/cern.ch/cms/generators/www <https://cms-project-generators.web.cern.ch/cms-project-generators/?C=M;O=A>`
2. Need four separate Madgraph cards (These are located in the Template directory:

  - \_customizecards.dat: 'where one would set the values of the parameters of the model, such as masses and couplings.'
  - \_extramodels.dat: 'if non-SM Lagrangians need to be used for the generations, must be declared and be uploaded to the generator web repository'
  - \_proc_card.dat: 'where one declares the process to be generated'
  - \_run_card.dat: 'where one defines particular options on how the generator will run and generate the process, as well as specific kinematic cut values '
3. in a CMSSW area in lxplus (i.e. CMSSW_7_1_21_patch1) the following directory should be created:
``git clone git@github.com:cms-sw/genproductions.git genproductions``
``cd genproductions/bin/MadGraph5_aMCatNLO/``
4. make the directories for all mass points/copy the Madgraph cards in corresponding directories / create script to create the gridpacks using lxbatch
``python dirGenerator_gridpack.py``
5. Before running ``sh create_submit_gridpack_generation.sh`` which will submit the jobs to lxbatch, it is better to run one sample locally and make sure that gridpack production is running OK. To do so run one line of the following ``create_gridpack_generation_script.sh``. i,e,
`./gridpack_generation.sh Codex_LQ1100_DM_450_X_520_gen2 cards/production/13TeV/DarkMatter_Codex/Codex_LQ1100_DM_450_X_520_gen2`
6. If the above step is fine, try to making some LE file first by doing the following:
``tar -xavf <path of gridpack creation>/XXX.tar.xz``
bash:
`./runcmsgrid.sh <nevents> <randomseed> <numberofcpus>`
The runcmsgrid.sh script requires 3 parameters: the first one is the number of events to be generated, the second one is a random seed and the third one is the number of CPUs.
7. in case LHE files seem OK, then this is the last step to create the full gridpack by submitting the jobs voia Lxbatch:
`sh create_submit_gridpack_generation.sh`

More information can be found here: <https://twiki.cern.ch/twiki/bin/viewauth/CMS/QuickGuideMadGraph5aMCatNLO>

--------------------------------------------------------------------
To get the LHE files wihout using the CMSSW do the following:
--------------------------------------------------------------------
To generate mixed signature for the leptoquark (1st generation), you can use:

`import model lq_met`
`define sm = u u~ d d~ e+ e- ve ve~`
`generate p p > m1 m1~ QCD=2 QED=0 NP=0, m1 > sm sm, (m1~ > ~dm ~x1~, ~x1~ > sm sm ~dm)`
`add process p p > m1 m1~ QCD=2 QED=0 NP=0, m1~ > sm sm, (m1 > ~dm ~x1, ~x1 > sm sm ~dm)`
`add process p p > m2 m2~ QCD=2 QED=0 NP=0, m2 > sm sm, (m2~ > ~dm ~x2~, ~x2~ > sm sm ~dm)`
`add process p p > m2 m2~ QCD=2 QED=0 NP=0, m2~ > sm sm, (m2 > ~dm ~x2, ~x2 > sm sm ~dm)`
`output pp_mm_mix_gen1_lq`

This set of commands creates the "MG5_aMC_v2_3_3/pp_mm_mix_gen1_lq" subdirectory, so after you exit the "MG5_aMC>" prompt (just type "exit"), you can move to this subdirectory.

Within this subdirectory, the file "Cards/param_card.dat" controls the dark matter, coannihilating partner, and mediator masses, as well as couplings of the mediator to the dark matter and to the SM. The dark matter mass is "MDM," the lighter and heavier components of the SU(2) multiplet of the coannihilating partner are "MX1" and "MX2," respectively, and the lighter and heavier components of the SU(2) multiplet of the leptoquark mediator are "MM1" and "MM2," respectively.

The Yukawa coupling of the mediator to the dark sector particles is "yD," and the Yukawa couplings of the leptoquark to the Q l_R structure are the "yQl1x1," "yQl2x2," "yQl3x3" numbers. Finally, the Yukawa couplings of the leptoquark to the L u_R structure are "yLu1x1," "yLu2x2," and "yLu3x3."

For your convenience, I've attached an edited param_card.dat which has the DM mass set to 300 GeV, the coannihilating partner masses set to 330 GeV, and the leptoquark mediator masses set to 1.2 TeV. The dark Yukawa coupling is 0.1, and the only nonzero mediator coupling to SM particles is yQl1x1 = 0.1414 = sqrt(2) / 10, which is one of the parameter points in Figure 22 of our paper [arXiv:1510.03434]. Please let me know if you have any questions about changing the model parameters.

Once you have your parameter card, the other important card to edit is "Cards/run_card.dat", which sets the sqrt(s) of the collider, the number of events, the PDF set, and any preselection cuts on jets, leptons, etc. that you like. For a first test, the default run_card should work, which will generate 10k events at 13 TeV LHC.

Finally, to generate events, go to the "MG5_aMC_v2_3_3/pp_mm_mix_gen1_lq/bin" directory, and type "./generate_events", which will give you a series of prompts to run additional modules like Pythia for showering and hadronization, PGS or Delphes for detector simulation, etc. You can just use "0" for all the prompts. The events should run and will show up in "pp_mm_mix_gen1_lq/Events/run_01/unweighted_events.lhe.gz". These can then be processed by Pythia for showering and hadronization as standard LHE format files.
