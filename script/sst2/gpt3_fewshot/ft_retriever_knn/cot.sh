#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# file: carp_davinci003.sh


PROJECT_PATH=/home/jovyan/SATD_Identification/CARP-Sun-2023/GPT-CLS-CARP
export PYTHONPATH="$PYTHONPATH:$PROJECT_PATH"


DATASET=sst2
MODEL=gpt3_fewshot
STRATEGY=ft_retriever_knn
SETTING=cot



for seed in 2333 # 8866 9998 6624 1314
do
  echo "=============================================================================="
  echo "SEED IS " ${seed}
  echo ${DATASET} "-" ${MODEL} "-" ${STRATEGY} "-" ${SETTING}
  echo "=============================================================================="
  python3 ${PROJECT_PATH}/task/gpt3_text_cls.py \
  --seed ${seed} --random \
  --config_path ${PROJECT_PATH}/configs/${DATASET}/${MODEL}/${STRATEGY}/${SETTING}.json \
  --step_idx 1-2-3-4
done

