import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from data_loading import load_data
from encoder_decoder import VAE_decoder, VAE_encoder, VAE
from tqdm.auto import tqdm
from pathlib import Path
import os
device = 'cuda' if torch.cuda.is_available() else 'cpu'
def main():
    # Reparameterization Trick

    # **Loss Function: Reconstruction + KL Divergence**
    def vae_loss(original, reconstructed, mu, log_var):
        reconstruction_loss = nn.functional.binary_cross_entropy(reconstructed, original, reduction='sum')
        kl_loss = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp())
        print(f'kl_loss: {kl_loss}')
        return reconstruction_loss + kl_loss

    # **Train Function**
    def train_vae(model, train_loader, epochs=5, learning_rate=0.1):
        optimizer = optim.Adam(model.parameters(), lr=learning_rate)
        model.train()

        for epoch in range(epochs):
            total_loss = 0
            print(f"\nEpoch {epoch+1}/{epochs} - Training started")

            for idx, (images, _) in enumerate(tqdm(train_loader, desc=f"Epoch {epoch+1} Progress")):
                images = images.to(device)

                optimizer.zero_grad()
                reconstructed, mu, log_var = model(images)
                
                loss = vae_loss(images, reconstructed, mu, log_var)
                loss.backward()
                optimizer.step()
                
                total_loss += loss.item()

                if idx % 100 == 0:  # Print progress every 100 batches
                    print(f"  Batch {idx}: Loss = {loss.item():.4f}")

            avg_loss = total_loss / len(train_loader)
            print(f"Epoch {epoch+1} completed. Average Loss: {avg_loss:.4f}")

    # **Run Training**
    train_loader, test_loader = load_data()
    encoder = VAE_encoder(
        input_layer = 3,
        latent_space_dim = 200,
        hidden_units = 128 
    )
    decoder = VAE_decoder(
        input_layer = 3,
        latent_space_dim = 200,
        hidden_units = 128 
    )
    vae = VAE(encoder, decoder).to(device)
    #print(vae)
    train = True
    path = 'generativeAI/weights/firstGen.weights.h5'

# Ensure directory exists before saving
    os.makedirs(os.path.dirname(path), exist_ok=True)

    if os.path.exists(path) and not train:
        print("Loading existing weights...")
        vae.load_state_dict(torch.load(path, weights_only=True))
    else:
        print("Training model and saving weights...") 
        train_vae(vae, train_loader, epochs = 5)
        # SAVE WEIGHTS
        torch.save(vae.state_dict(), path)
        print("Weights saved successfully.")


    # Predictions
    # Get a batch of test images
    sample_x, _ = next(iter(test_loader))
    sample_x = sample_x.to(device)

    # Get VAE predictions (reconstructions)
    vae.eval()
    with torch.inference_mode():
        reconstructed, _, _ = vae(sample_x)

    # Select 16 random indices
    random_idx = torch.randint(0, len(sample_x), size=(16,))

    # Plot originals and reconstructions
    fig, axes = plt.subplots(4, 8, figsize=(12, 6))  # 4 rows, 8 columns (original | reconstructed)

    for idx, i in enumerate(random_idx):
        # Original image
        orig_img = sample_x[i].cpu().permute(1, 2, 0)
        axes[idx // 4, (idx % 4) * 2].imshow(orig_img)
        axes[idx // 4, (idx % 4) * 2].set_title("Original")
        axes[idx // 4, (idx % 4) * 2].axis(False)

        # Reconstructed image
        recon_img = reconstructed[i].cpu().permute(1, 2, 0)
        axes[idx // 4, (idx % 4) * 2 + 1].imshow(recon_img)
        axes[idx // 4, (idx % 4) * 2 + 1].set_title("Reconstructed")
        axes[idx // 4, (idx % 4) * 2 + 1].axis(False)

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()