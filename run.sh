#!/usr/bin/env bash
# Set bash to 'debug' mode, it will exit on :
# -e 'error', -u 'undefined variable', -o ... 'error in pipeline', -x 'print commands',
set -e
set -u
set -o pipefail

tag=test1
raw_feats_directory=/home/hdd/lip_visual/220812_camera_speller_512_from_espnet1

. ../../../tools/activate_python.sh 

train_set=train
valid_set=val
test_sets=test

. asr.sh \
    --raw_feats_dir "${raw_feats_directory}" \
    --pretrain false \
    --lang "en" \
    --use_lm false \
    --token_type char \
    --lm_config conf/train_lm_transformer.yaml \
    --asr_config conf/train_asr_transformer.yaml \
    --inference_config conf/decode.yaml \
    --train_set "${train_set}" \
    --valid_set "${valid_set}" \
    --test_sets "${test_sets}" \
    --bpe_train_text "data/train/text" \
    --lm_train_text "data/train/text data/val/text" "$@" \
    --expdir "${raw_feats_directory}"/exp \
    --asr_tag "${tag}" \
    
    # --nlsyms_txt data/nlsyms.txt \