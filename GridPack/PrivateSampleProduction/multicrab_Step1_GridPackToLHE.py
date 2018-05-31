from WMCore.Configuration import Configuration

config = Configuration()
config.section_("General")
#config.General.requestName   = 'DM_Codex_1800_600_600' #task-dependent
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'PrivateMC'
#config.JobType.inputFiles = ['Codex_LQ1800_DM_600_X_600_gen2_tarball.tar.xz']
#config.JobType.psetName    = 'wmLHE_DM_LQ_1000_400_440_cfg.py' #this is the config file you created with cmsDriver

config.section_("Data")
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500 #task-dependent - set up to make just one output file
config.Data.totalUnits  = 50000 #task-dependent
config.Data.publication = True
config.Data.outLFNDirBase = '/store/user/oneogi/CodexGP'

# These strings are used to construct the output dataset name
config.Data.outputDatasetTag  = 'wmLHE' #something you like
#config.Data.outputPrimaryDataset  = 'DM_Codex_1000_400_440' #this is the dataset name that all tiers will have.  e.g. VBFHToBB_M-125_13TeV_powheg_pythia8

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC' # Where the output files will be transmitted to



if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea = 'crab_projects3'

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################


    Sample=['1600_700_770', '1600_700_805', '1700_600_600', '1000_400_420', '1000_400_440', '1000_400_460', '1100_450_475', '1100_450_495', '1100_450_520', '1200_500_525', '1200_500_550', '1200_500_575', '1200_600_600', '1300_550_580', '1300_550_605', '1300_550_635', '1300_600_600', '1400_600_600', '1400_600_630', '1400_600_660', '1400_600_690', '1500_600_600', '1500_650_685', '1500_650_715', '1500_650_750', '1600_600_600', '1600_700_735', '1700_750_790', '1700_750_825', '1700_750_865', '1800_600_600', '1800_800_840', '1800_800_880', '1800_800_920', '1900_850_895', '1900_850_935', '1900_850_975', '2000_900_990', '800_300_330', '900_350_385']

    for sam in Sample:
        config.General.requestName   = 'DM_Codex_%s'%sam #task-dependent
        samSp = sam.split('_')
        config.JobType.inputFiles = ['Codex_LQ%s_DM_%s_X_%s_gen2_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'%(samSp[0],samSp[1],samSp[2])] #Input Files
        config.JobType.psetName    = 'wmLHE_DM_LQ_%s_cfg.py'%sam #this is the config file you created with cmsDriver
        config.Data.outputPrimaryDataset  = 'DM_Codex_%s'%sam #this is the dataset name that all tiers will have.  e.g. VBFHToBB_M-125_13TeV_powheg_pythia8
        print config
        submit(config)

'''
    config.General.requestName   = 'DM_Codex_1600_700_770' #task-dependent
    config.JobType.inputFiles = ['Codex_LQ1600_DM_700_X_770_gen2_tarball.tar.xz']
    config.JobType.psetName    = 'wmLHE_DM_LQ_1200_500_550_cfg.py' #this is the config file you created with cmsDriver
    config.Data.outputPrimaryDataset  = 'DM_Codex_1200_500_550' #this is the dataset name that all tiers will have.  e.g. VBFHToBB_M-125_13TeV_powheg_pythia8
    submit(config)
'''
