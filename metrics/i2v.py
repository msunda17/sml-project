import torch
from diffusers import I2VGenXLPipeline
from diffusers.utils import export_to_gif, load_image
pipeline = I2VGenXLPipeline.from_pretrained("ali-vilab/i2vgen-xl", torch_dtype=torch.float16, variant="fp16")
pipeline.enable_model_cpu_offload()
# image_url = "https://huggingface.co/datasets/diffusers/docs-images/resolve/main/i2vgen_xl_images/img_0009.png"
image_url = "./driving_car/car_2.png"
image = load_image(image_url).convert("RGB")
# prompt = "baby racoon shaking its head and blinking its eyes"
prompt = "driving car"
# negative_prompt = "Distorted, discontinuous, Ugly, blurry, low resolution, motionless, static, disfigured, disconnected limbs, Ugly faces, incomplete arms"
generator = torch.manual_seed(8888)
frames = pipeline(
    prompt=prompt,
    image=image,
    num_inference_steps=25,
    # negative_prompt=negative_prompt,
    guidance_scale=12.5,
    generator=generator
).frames[0]
video_path = export_to_gif(frames, "./driving_car_video/car_2.gif")