import sys
import ROOT as root

if len(sys.argv)<2:
    print("Need filename as first Input")
else:
    fileList = open(sys.argv[1], 'r')
    firstFile = True
    for fileNumber,fileName in enumerate(fileList):
        fileName = fileName.rstrip()
        # fileName = "ROOT_PreSelection_SingleEleEleJet_LepPt_MT0_HighDPhi_Iso.root"
        print(fileName)
        # mtCut = fileName.split("_")[4][2:]
        c1 = root.TCanvas( "Background", "Background", 200, 10, 700, 500 )

        f = root.TFile.Open(fileName, "READ")

        histograms = [f.Get("EleJet/W"), f.Get("EleJet/ZTT"),
                      f.Get("EleJet/SingleTop"), f.Get("EleJet/TT")]
        stack = root.THStack("Background Samples:","Background Samples:")

        colors = [1, 2, 3, 4]

        legendPosition=[0.709,0.508,0.883,0.759]
        legendEntries=["W", "ZTT", "SingleTop", "TT"]
        legend = root.TLegend(legendPosition[0], legendPosition[1], legendPosition[2], legendPosition[3])

        rebin=[20,20,2]
        ranges = [1300,600,700]

        xTitle = ["Jet PT (GeV)", "Lepton PT (GeV)", "MET (GeV)"]
        yTitle = "No. Events"
        wipLabel = root.TText(.54,.85,"CMS Work In Progress")
        wipLabel.SetNDC(root.kTRUE)

        for i,histogram in enumerate(histograms):
            histogram.Rebin(rebin[fileNumber])
            histogram.SetLineColor(root.kBlack)
            histogram.SetFillColor(colors[i])

            stack.Add(histogram)

            if (i==0):
                yMax = histogram.GetMaximum()
            elif (yMax<histogram.GetMaximum()):
                yMax = histogram.GetMaximum()

            legend.AddEntry(histogram,legendEntries[i],"f")

        stack.Draw("HIST")
        stack.SetMaximum(yMax+yMax/10)
        root.gPad.SetLogy()

        stack.GetXaxis().SetRangeUser(0,ranges[fileNumber])


        root.gStyle.SetOptStat(0)

        legend.SetFillColor(root.kWhite)
        legend.SetBorderSize(0)
        legend.SetTextSize(0.043)

        wipLabel.Draw()
        legend.Draw()

        stack.GetYaxis().SetTitleSize(0.04)
        stack.GetYaxis().SetTitleOffset(1.2)
        stack.GetYaxis().SetLabelSize(0.04)
        stack.GetXaxis().SetTitleSize(0.04)
        stack.GetXaxis().SetTitleOffset(1)
        stack.GetXaxis().SetLabelSize(0.04)
        stack.GetYaxis().SetTitle(yTitle)
        stack.GetXaxis().SetTitle(xTitle[fileNumber])

        c1.SaveAs("./Bg_" + fileName.split("_")[3] + ".png")
# root.gApplication.Run()
