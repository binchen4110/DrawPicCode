import torch
import numpy as np


# 计算beta方式
def linear_beta_schedule(timesteps, beta_start, beta_end):
    beta_start = beta_start
    beta_end = beta_end
    return torch.linspace(beta_start, beta_end, timesteps)

def cosine_beta_schedule(timesteps, s=0.008):
    steps = timesteps + 1
    x = torch.linspace(0, timesteps, steps)
    alphas_cumprod = torch.cos(((x / timesteps) + s) / (1 + s) * torch.pi * 0.5) ** 2
    alphas_cumprod = alphas_cumprod / alphas_cumprod[0]
    betas = 1 - (alphas_cumprod[1:] / alphas_cumprod[:-1])
    return torch.clip(betas, 0.0001, 0.9999)

def exp_beta_schedule(timesteps, beta_min=0.1, beta_max=10):
    x = torch.linspace(1, 2 * timesteps + 1, timesteps)
    betas = 1 - torch.exp(- beta_min / timesteps - x * 0.5 * (beta_max - beta_min) / (timesteps * timesteps))
    return betas

# sqrt
def betas_for_alpha_bar(num_diffusion_timesteps, alpha_bar, max_beta=0.999):
    """
    Create a beta schedule that discretizes the given alpha_t_bar function,
    which defines the cumulative product of (1-beta) over time from t = [0,1].
    :param num_diffusion_timesteps: the number of betas to produce.
    :param alpha_bar: a lambda that takes an argument t from 0 to 1 and
                      produces the cumulative product of (1-beta) up to that
                      part of the diffusion process.
    :param max_beta: the maximum beta to use; use values lower than 1 to
                     prevent singularities.
    """
    betas = []
    for i in range(num_diffusion_timesteps):
        t1 = i / num_diffusion_timesteps
        t2 = (i + 1) / num_diffusion_timesteps
        betas.append(min(1 - alpha_bar(t2) / alpha_bar(t1), max_beta))
    return np.array(betas)

beta_start = 1e-4
beta_end = 0.02
steps = 200
beta_sche = "exp"

if beta_sche == 'linear':
    betas = linear_beta_schedule(timesteps=steps, beta_start=beta_start, beta_end=beta_end)
elif beta_sche == 'exp':
    betas = exp_beta_schedule(timesteps=steps)
elif beta_sche == 'cosine':
    betas = cosine_beta_schedule(timesteps=steps)
elif beta_sche == 'sqrt':
    betas = torch.tensor(betas_for_alpha_bar(steps, lambda t: 1 - np.sqrt(t + 0.0001), )).float()
else:
    raise NotImplementedError()

alphas = 1.0 - betas
alphas_cumprod = np.cumprod(alphas, axis=0)  # alpha_bar

print(alphas_cumprod)