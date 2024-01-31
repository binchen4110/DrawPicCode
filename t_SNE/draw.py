# import torch
# import numpy as np
# from model import DiffCas
# from parsers import parser
#
# def init_seeds(seed=2023):
#     torch.manual_seed(seed)
#     torch.cuda.manual_seed(seed)
#     torch.cuda.manual_seed_all(seed)
#     np.random.seed(seed)
#     torch.backends.cudnn.deterministic = True
#
# init_seeds(seed=2023)
#
# def print_some_weights(model):
#     print("user_embeddings:\n", model.user_embeddings.weight.data)
#     print("classifier_noib_past:\n", model.classifier_noib_past.weight.data)
#
# opt = parser.parse_args()
# opt.user_size = 12629
# opt.save_path = f"./checkpoint/{opt.data_name}/lr_{opt.lr}_batch_{opt.batch_size}_step_{opt.steps}_emb_{opt.hidden_size}.pt"
# opt.compress_emb = int(opt.hidden_size * 0.75)
# model = DiffCas(opt).cuda()
#
# # 加载权重文件
# weights = torch.load("/home/icdm/ywx/diffcas7/checkpoint/twitter/lr_0.005_batch_32_step_32_emb_64.pt")
#
# # 将权重文件应用到模型上
# saved_state_dict = torch.load("/home/icdm/ywx/diffcas7/checkpoint/twitter/lr_0.005_batch_32_step_32_emb_64.pt")
#
#
# user_embeddings_params = {k: v for k, v in saved_state_dict.items() if 'user_embeddings' in k}
#
#
# print(0)