import sys
import ROOT as root
from DataFormats.FWLite import Events, Handle
import math


def getMT(pt, px, py, met, metPhi):
    return math.sqrt(math.pow(pt + met, 2) - math.pow(px + met * math.cos(metPhi), 2) - math.pow(py + met * math.sin(metPhi), 2))

if len(sys.argv) < 2:
    print("Need input filelist as first Input")
elif len(sys.argv) < 3:
    print("Need output filename as second Input")
else:
    fileList = open(sys.argv[1], 'r')
    firstFile = True

    leptonPT = root.TH1F("leptonPT", "leptonPT", 200, 0, 2000)
    MET = root.TH1F("MET", "MET", 200, 0, 2000)
    JetPT = root.TH1F("JetPT", "JetPT", 200, 0, 2000)
    LQMT = root.TH1F("LQMT", "LQMT", 200, 0, 2000)

    leptonPT1000 = root.TH1F("leptonPT1000", "leptonPT1000",80, 0, 2000)
    MET1000 = root.TH1F("MET1000", "MET1000",80, 0, 2000)
    JetPT1000 = root.TH1F("JetPT1000", "JetPT1000", 200, 0, 2000)
    LQMT1000 = root.TH1F("LQMT1000", "LQMT1000", 2000, 0, 2000)

    leptonPT1200 = root.TH1F("leptonPT1200", "leptonPT1200",80, 0, 2000)
    MET1200 = root.TH1F("MET1200", "MET1200", 200, 0, 2000)
    JetPT1200 = root.TH1F("JetPT1200", "JetPT1200", 200, 0, 2000)
    LQMT1200 = root.TH1F("LQMT1200", "LQMT1200", 2000, 0, 2000)

    leptonPT1400 = root.TH1F("leptonPT1400", "leptonPT1400",80, 0, 2000)
    MET1400 = root.TH1F("MET1400", "MET1400", 200, 0, 2000)
    JetPT1400 = root.TH1F("JetPT1400", "JetPT1400", 200, 0, 2000)
    LQMT1400 = root.TH1F("LQMT1400", "LQMT1400", 2000, 0, 2000)

    leptonPT1600 = root.TH1F("leptonPT1600", "leptonPT1600",80, 0, 2000)
    MET1600 = root.TH1F("MET1600", "MET1600", 200, 0, 2000)
    JetPT1600 = root.TH1F("JetPT1600", "JetPT1600", 200, 0, 2000)
    LQMT1600 = root.TH1F("LQMT1600", "LQMT1600", 2000, 0, 2000)

    leptonPT1800 = root.TH1F("leptonPT1800", "leptonPT1800",80, 0, 2000)
    MET1800 = root.TH1F("MET1800", "MET1800", 200, 0, 2000)
    JetPT1800 = root.TH1F("JetPT1800", "JetPT1800", 200, 0, 2000)
    LQMT1800 = root.TH1F("LQMT1800", "LQMT1800", 2000, 0, 2000)

    leptonPT2000 = root.TH1F("leptonPT2000", "leptonPT2000",80, 0, 2000)
    MET2000 = root.TH1F("MET2000", "MET2000", 200, 0, 2000)
    JetPT2000 = root.TH1F("JetPT2000", "JetPT2000", 200, 0, 2000)
    LQMT2000 = root.TH1F("LQMT2000", "LQMT2000", 2000, 0, 2000)

    for fileName in fileList:
        fileName = fileName.rstrip()

        events = Events(fileName)

        # create handle outside of loop
        hndl_muons = Handle("vector<pat::Muon>")
        hndl_met = Handle("vector<pat::MET>")
        hndl_jets = Handle("vector<pat::Jet>")

        label_met = ("slimmedMETs")
        label_muons = ("slimmedMuons")
        label_jets = ("slimmedJets")

        root.gROOT.SetBatch()

        for event in events:
            event.getByLabel(label_met, hndl_met)
            event.getByLabel(label_muons, hndl_muons)
            event.getByLabel(label_jets, hndl_jets)

            muon = hndl_muons.product()
            met = hndl_met.product()
            jet = hndl_jets.product()

            if (not muon.size()) or (not met.size()) or (not jet.size()):
                continue

            muon = muon[0]
            met = met[0]
            jet = jet[0]

            if (muon.pt()<60 or muon.eta()>2.5) or (jet.pt()<100 or jet.eta()>2.5) or (met.pt()<50):
                continue

            muon4Momentum = root.TLorentzVector()
            muon4Momentum.SetPtEtaPhiE(muon.pt(), muon.eta(), muon.phi(), muon.energy())

            jet4Momentum = root.TLorentzVector()
            jet4Momentum.SetPtEtaPhiE(jet.pt(), jet.eta(), jet.phi(), jet.energy())

            LQ4Momentum = jet4Momentum + muon4Momentum

            mt = LQ4Momentum.M()
            # mt = getMT(LQ4Momentum.Pt(), LQ4Momentum.Px(),LQ4Momentum.Py(), met.pt(), met.phi())

            if mt > 250:
                leptonPT.Fill(muon.pt())
                MET.Fill(met.pt())
                JetPT.Fill(jet.pt())
                LQMT.Fill(mt)

            if mt > 1000:
                leptonPT1000.Fill(muon.pt())
                MET1000.Fill(met.pt())
                JetPT1000.Fill(jet.pt())
                LQMT1000.Fill(mt)

            if mt > 1200:
                leptonPT1200.Fill(muon.pt())
                MET1200.Fill(met.pt())
                JetPT1200.Fill(jet.pt())
                LQMT1200.Fill(mt)

            if mt > 1400:
                leptonPT1400.Fill(muon.pt())
                MET1400.Fill(met.pt())
                JetPT1400.Fill(jet.pt())
                LQMT1400.Fill(mt)

            if mt > 1600:
                leptonPT1600.Fill(muon.pt())
                MET1600.Fill(met.pt())
                JetPT1600.Fill(jet.pt())
                LQMT1600.Fill(mt)

            if mt > 1800:
                leptonPT1800.Fill(muon.pt())
                MET1800.Fill(met.pt())
                JetPT1800.Fill(jet.pt())
                LQMT1800.Fill(mt)

            if mt > 2000:
                leptonPT2000.Fill(muon.pt())
                MET2000.Fill(met.pt())
                JetPT2000.Fill(jet.pt())
                LQMT2000.Fill(mt)

    output = root.TFile.Open(sys.argv[2], "RECREATE")

    leptonPT.Write()
    MET.Write()
    JetPT.Write()
    LQMT.Write()

    leptonPT1000.Write()
    MET1000.Write()
    JetPT1000.Write()
    LQMT1000.Write()

    leptonPT1200.Write()
    MET1200.Write()
    JetPT1200.Write()
    LQMT1200.Write()

    leptonPT1400.Write()
    MET1400.Write()
    JetPT1400.Write()
    LQMT1400.Write()

    leptonPT1600.Write()
    MET1600.Write()
    JetPT1600.Write()
    LQMT1600.Write()

    leptonPT1800.Write()
    MET1800.Write()
    JetPT1800.Write()
    LQMT1800.Write()

    leptonPT2000.Write()
    MET2000.Write()
    JetPT2000.Write()
    LQMT2000.Write()
