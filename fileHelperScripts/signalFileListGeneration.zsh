dasgoclient -query='file dataset=/DM_Codex_1000_400_440/abdollah-MiniAODv2-b59cb78551aff289588aa5c69db4a3a1/USER instance=prod/phys03' > fl.tmp
awk '{print "root://cmsxrootd.fnal.gov/"$0 }' fl.tmp > DM_1000_400_440_FL.txt
dasgoclient -query='file dataset=/DM_Codex_1200_500_550/abdollah-MiniAODv2-b59cb78551aff289588aa5c69db4a3a1/USER instance=prod/phys03' > fl.tmp
awk '{print "root://cmsxrootd.fnal.gov/"$0 }' fl.tmp > DM_1200_500_550_FL.txt
dasgoclient -query='file dataset=/DM_Codex_1400_600_660/abdollah-MiniAODv2-b59cb78551aff289588aa5c69db4a3a1/USER instance=prod/phys03' > fl.tmp
awk '{print "root://cmsxrootd.fnal.gov/"$0 }' fl.tmp > DM_1400_600_660_FL.txt
dasgoclient -query='file dataset=/DM_Codex_1600_700_770/abdollah-MiniAODv2-b59cb78551aff289588aa5c69db4a3a1/USER instance=prod/phys03' > fl.tmp
awk '{print "root://cmsxrootd.fnal.gov/"$0 }' fl.tmp > DM_1600_700_770_FL.txt
dasgoclient -query='file dataset=/DM_Codex_1800_800_880/abdollah-MiniAODv2-b59cb78551aff289588aa5c69db4a3a1/USER instance=prod/phys03' > fl.tmp
awk '{print "root://cmsxrootd.fnal.gov/"$0 }' fl.tmp > DM_1800_800_880_FL.txt
dasgoclient -query='file dataset=/DM_Codex_2000_900_990/abdollah-MiniAODv2-b59cb78551aff289588aa5c69db4a3a1/USER instance=prod/phys03' > fl.tmp
awk '{print "root://cmsxrootd.fnal.gov/"$0 }' fl.tmp > DM_2000_900_990_FL.txt
rm fl.tmp