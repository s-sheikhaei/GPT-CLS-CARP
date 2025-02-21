#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# file: save_nearest_neighbors.sh


PROJECT_PATH=/home/jovyan/SATD_Identification/CARP-Sun-2023/GPT-CLS-CARP
export PYTHONPATH="$PYTHONPATH:$PROJECT_PATH"

FOLD=0
DATA_DIR=/home/jovyan/SATD_Identification/CARP-Sun-2023/data/obrien/fold_${FOLD}
MLM_DIR="roberta-large"
CKPT_PATH="/home/jovyan/SATD_Identification/CARP-Sun-2023/outputs/trained_models/obrien_roberta_large/epoch8_bs16_lr2e-5_weightdecay0.05_warmup0.06_maxlen512_dropout0.2_grad1/checkpoint/epoch=4-val_loss=1.0962-val_acc=0.6709.ckpt"
CANDI_TYPE=train
THRESHOLD=0.0
TOPK=24
RANKING=finetuned_roberta-large
MAX_LEN=280
DATA_SIGN=obrien

# 2333, 8866, 1314, 6624, 9998

SEED=9998
QUERY_TYPE=test
SAVE_PATH=/home/jovyan/SATD_Identification/CARP-Sun-2023/outputs/nearest_neighbors/${DATA_SIGN}/test_${RANKING}_cand${CANDI_TYPE}_thres${THRESHOLD}_top${TOPK}_seed${SEED}_fold${FOLD}.jsonl


CUDA_VISIBLE_DEVICES=0 python3 ${PROJECT_PATH}/task/save_nearest_neighbors.py \
--seed ${SEED} \
--data_dir ${DATA_DIR} \
--mlm_dir ${MLM_DIR} \
--encoder_ckpt_path ${CKPT_PATH} \
--candidate_type ${CANDI_TYPE} \
--query_type ${QUERY_TYPE} \
--search_threshold ${THRESHOLD} \
--top_k ${TOPK} \
--ranking_model ${RANKING} \
--save_nearest_neighbor_path ${SAVE_PATH} \
--dataset_name ${DATA_SIGN} \
--max_len ${MAX_LEN}

# RANKING=sup_simcse_roberta-large
# SAVE_PATH=/home/jovyan/SATD_Identification/CARP-Sun-2023/nearest_neighbors/sst2_nearest_neighbors/test_${RANKING}_cand${CANDI_TYPE}_thres${THRESHOLD}_top${TOPK}_seed${SEED}.jsonl

# CUDA_VISIBLE_DEVICES=1 python3 ${PROJECT_PATH}/task/save_nearest_neighbors.py \
# --seed ${SEED} \
# --data_dir ${DATA_DIR} \
# --mlm_dir ${MLM_DIR} \
# --encoder_ckpt_path ${CKPT_PATH} \
# --candidate_type ${CANDI_TYPE} \
# --query_type ${QUERY_TYPE} \
# --search_threshold ${THRESHOLD} \
# --top_k ${TOPK} \
# --ranking_model ${RANKING} \
# --save_nearest_neighbor_path ${SAVE_PATH} \
# --max_len ${MAX_LEN} \
# --retriever_type "simcse"


