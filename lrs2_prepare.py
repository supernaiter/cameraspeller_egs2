#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    raw_feats_dir = sys.argv[1]
    pretrain = sys.argv[2].lower()
    # with open(f"{raw_feats_dir}/lrs2_transcript.txt","r") as t:
    #with open(f"{raw_feats_dir}/lrs2_transcript_no_digits.txt","r") as t:
    with open(f"{raw_feats_dir}/transcription.txt","r") as t:
    # with open(f"{raw_feats_dir}/lrs2_viseme_transcript.txt","r") as t:
        txt = t.readlines()
    text_dict = dict()
    for t in txt:
        utt, text = t.split(" ",1)
        utt = utt.replace("/","-")
        text_dict[utt] = text.strip()

    for dataset in ["train","val","test"]:
        utts = []
        texts = []
        scps = []
        with open(f"{raw_feats_dir}/{dataset}.scp","r") as s:
            scps_ = s.readlines()
            for s in scps_:
                utt = s.split(" ")[0].replace("/","-")
                utts.append(utt)
                texts.append(text_dict[utt])
                scps.append(utt + " " + s.split(" ")[1] )
        if dataset == "train" and pretrain=="true":
            with open(f"{raw_feats_dir}/pretrain.scp","r") as s:
                scps_ = s.readlines()
                for s in scps_:
                    utt = s.split(" ")[0].replace("/","-")
                    utts.append(utt)
                    texts.append(text_dict[utt])
                    scps.append(utt + " " + s.split(" ")[1] )
        dataset_dir = f"data/{dataset}"
        n_utts = len(utts)

        spk2utt = "LRS2 " + " ".join(utts)
        utt2spk = []
        wav = []

        for i in range(n_utts):
            utt2spk.append(utts[i] + " LRS2\n")
            wav.append(utts[i] + " " + str(i) + ".wav\n")
        with open(dataset_dir + "/feats.scp", "w") as s:
            s.writelines(scps)
        with open(dataset_dir + "/text", "w") as t:
            for i in range(n_utts):
                t.write(f"{utts[i]} {texts[i]}\n")
        with open(dataset_dir + "/spk2utt", "w") as s:
            s.writelines(spk2utt)
        with open(dataset_dir + "/utt2spk", "w") as u:
            u.writelines(utt2spk)
        with open(dataset_dir + "/wav.scp", "w") as w:
            w.writelines(wav)
        