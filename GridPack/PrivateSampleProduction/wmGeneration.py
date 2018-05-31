from string import Template
#File Manipulation
filein = open('wmLHE_DM_LQ_TEMPLATE_cfg.py')
src = Template( filein.read() )

massPoints = ['1600_700_770', '1600_700_805', '1700_600_600', '1000_400_420', '1000_400_440', '1000_400_460', '1100_450_475', '1100_450_495', '1100_450_520', '1200_500_525', '1200_500_550', '1200_500_575', '1200_600_600', '1300_550_580', '1300_550_605', '1300_550_635', '1300_600_600', '1400_600_600', '1400_600_630', '1400_600_660', '1400_600_690', '1500_600_600', '1500_650_685', '1500_650_715', '1500_650_750', '1600_600_600', '1600_700_735', '1700_750_790', '1700_750_825', '1700_750_865', '1800_600_600', '1800_800_840', '1800_800_880', '1800_800_920', '1900_850_895', '1900_850_935', '1900_850_975', '2000_900_990', '800_300_330', '900_350_385']

for point in massPoints:
    #filename Generation
    point = point.split("_")
    fileName='Codex_LQ%s_DM_%s_X_%s_gen2_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'%(point[0],point[1],point[2])

    #substitution
    d={'fileName':fileName}
    result = src.substitute(d)

    #Writing output
    f = open('wmLHE_DM_LQ_%s_cfg.py'%("_".join(point)), 'w+')
    f.write(result)
    f.close
