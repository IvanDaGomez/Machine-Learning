import torch
from torch import nn


class VAE_encoder(nn.Module):
    def __init__(self, 
                 input_layer, 
                 hidden_units, 
                 latent_space_dim):
        super().__init__()
        self.input_layer = input_layer
        self.hidden_units = hidden_units

        self.latent_space_dim = latent_space_dim
        self.conv_block_1 = nn.Sequential(
            nn.Conv2d(in_channels = self.input_layer, 
                      out_channels = self.hidden_units, 
                      kernel_size=3, 
                      stride=2, 
                      padding=1),
            nn.BatchNorm2d(num_features = self.hidden_units),
            nn.LeakyReLU()
        )

        self.conv_block_2 = nn.Sequential(
            nn.Conv2d(in_channels = self.hidden_units, 
                      out_channels = self.hidden_units, 
                      kernel_size=3, 
                      stride=2, 
                      padding=1),
            nn.BatchNorm2d(num_features = self.hidden_units),
            nn.LeakyReLU()
        )

        self.conv_block_3 = nn.Sequential(
            nn.Conv2d(in_channels = self.hidden_units, 
                      out_channels = self.hidden_units, 
                      kernel_size=3, 
                      stride=2, 
                      padding=1),
            nn.BatchNorm2d(num_features = self.hidden_units),
            nn.LeakyReLU()
        )

        self.conv_block_4 = nn.Sequential(
            nn.Conv2d(in_channels = self.hidden_units, 
                      out_channels = self.hidden_units, 
                      kernel_size=3, 
                      stride=2, 
                      padding=1),
            nn.BatchNorm2d(num_features = self.hidden_units),
            nn.LeakyReLU()
        )

        self.final_layer = nn.Sequential(
            nn.Flatten(),
            nn.Linear(in_features = 512 * 4, out_features = self.latent_space_dim),
            nn.Linear(in_features = self.latent_space_dim, out_features = self.latent_space_dim),
            nn.Sigmoid()
        )
    # def forward(self, X):
    #     #print(f"Input shape: {X.shape}")  # Initial input tensor shape
        
    #     X = self.conv_block_1(X)
    #     #print(f"After conv_block_1: {X.shape}")  # After first convolutional + activation + pooling

    #     X = self.conv_block_2(X)
    #     #print(f"After conv_block_2: {X.shape}")  # After second convolutional block

    #     X = self.conv_block_3(X)
    #     #print(f"After conv_block_3: {X.shape}")  # After third convolutional block

    #     X = self.conv_block_4(X)
    #     #print(f"After conv_block_4: {X.shape}")  # After fourth convolutional block

    #     X = self.final_layer(X)
    #     #print(f"After final_layer: {X.shape}")  # Output shape (likely latent space in VAE)
    #     X = torch.sigmoid(X)
    #     return X
    def forward(self, X): return torch.sigmoid(self.final_layer(self.conv_block_4(self.conv_block_3(self.conv_block_2(self.conv_block_1(X))))))

    # def forward(self, X):
    #     return self.final_layer(self.conv_block_4(self.conv_block_3(self.conv_block_2(self.conv_block_1(X)))))



class VAE_decoder(nn.Module):
    def __init__(self, 
                 input_layer, 
                 hidden_units, 
                 latent_space_dim):
        super().__init__()
        self.input_layer = input_layer
        self.hidden_units = hidden_units
        self.latent_space_dim = latent_space_dim
        self.initial_layer = nn.Sequential(
            nn.Linear(latent_space_dim, 512 * 4),
            nn.BatchNorm1d(num_features = 512 * 4),
            nn.LeakyReLU(),
            nn.Unflatten(1, (128, 4, 4))
        )
        self.conv_block_1 = nn.Sequential(
            nn.ConvTranspose2d(in_channels = self.hidden_units, 
                      out_channels = self.hidden_units, 
                      kernel_size=3, 
                      stride=2, 
                      padding=1,
                      output_padding = 1),
            nn.BatchNorm2d(num_features = self.hidden_units),
            nn.LeakyReLU()
        )

        self.conv_block_2 = nn.Sequential(
            nn.ConvTranspose2d(in_channels = self.hidden_units, 
                      out_channels = self.hidden_units, 
                      kernel_size=3, 
                      stride=2, 
                      padding=1,
                      output_padding = 1),
            nn.BatchNorm2d(num_features = self.hidden_units),
            nn.LeakyReLU()
        )

        self.conv_block_3 = nn.Sequential(
            nn.ConvTranspose2d(in_channels = self.hidden_units, 
                      out_channels = self.hidden_units, 
                      kernel_size=3, 
                      stride=2, 
                      padding=1,
                      output_padding = 1),
            nn.BatchNorm2d(num_features = self.hidden_units),
            nn.LeakyReLU()
        )

        self.conv_block_4 = nn.Sequential(
            nn.ConvTranspose2d(in_channels = self.hidden_units, 
                      out_channels = self.input_layer, 
                      kernel_size=3, 
                      stride=2, 
                      padding=1,
                      output_padding = 1),
            nn.BatchNorm2d(num_features = self.input_layer),
            nn.LeakyReLU()
        )
    # def forward(self, X):
    #     #print(f"Before initial_layer (input processing): {X.shape}")
    #     X = self.initial_layer(X)
    #     #print(f"After initial_layer (input processing): {X.shape}")  # Initial preprocessing layer

    #     X = self.conv_block_1(X)
    #     #print(f"After conv_block_1 (first convolutional block): {X.shape}")

    #     X = self.conv_block_2(X)
    #     #print(f"After conv_block_2 (second convolutional block): {X.shape}")

    #     X = self.conv_block_3(X)
    #     #print(f"After conv_block_3 (third convolutional block): {X.shape}")

    #     X = self.conv_block_4(X)
    #     #print(f"Output shape: {X.shape}")
    #     X = torch.sigmoid(X)
    #     return X
    def forward(self, X): return torch.sigmoid(self.conv_block_4(self.conv_block_3(self.conv_block_2(self.conv_block_1(self.initial_layer(X))))))

    # def forward(self, X):
    #     return self.final_layer(self.conv_block_4(self.conv_block_3(self.conv_block_2(self.conv_block_1(self.initial_layer(X))))))

class Sampling(nn.Module):
    def forward(self, mu, log_var):
        std = torch.exp(0.5 * log_var)  # Compute standard deviation
        eps = torch.randn_like(std)  # Sample epsilon from standard normal
        return mu + eps * std  # Reparameterized latent vector

    # **VAE Model**
class VAE(nn.Module):
    def __init__(self, encoder, decoder, latent_dim=200):
        super(VAE, self).__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.mu_layer = nn.Linear(latent_dim, 1024)  # Mean μ
        self.mu_output_layer = nn.Linear(1024, latent_dim)
        self.log_var_layer = nn.Linear(latent_dim, 1024)  # Log Variance logσ²
        self.log_var_output_layer = nn.Linear(1024, latent_dim)
        
        self.sampling = Sampling()
    def forward(self, x):
        #print(f'Input shape: {x.shape}')
        encoded = self.encoder(x)
        #print(f'Encoder output shape: {encoded.shape}')
        mu = self.mu_layer(encoded)  # Compute mean
        #print(f'mu layer: {mu.shape}')
        mu = self.mu_output_layer(mu)
        #print(f'mu layer: {mu.shape}')
        log_var = self.log_var_layer(encoded)  # Compute log variance
        log_var = self.log_var_output_layer(log_var)
        print(f'Log_var: {log_var}')
        log_var = torch.clamp(log_var, min=-10, max=10) 

        #print(f'log_var layer: {mu.shape}')
        z = self.sampling(mu, log_var)  # Sample using reparameterization trick
        
        reconstructed = self.decoder(z)  # Decode back to image
        print("Reconstructed min:", reconstructed.min().item(), "max:", reconstructed.max().item())
        print("Original min:", x.min().item(), "max:", x.max().item())
        return reconstructed, mu, log_var
    # def forward(self, x): 
        
    #     return self.decoder(self.sampling(self.mu_output_layer(self.mu_layer(self.encoder(x))), self.log_var_output_layer(self.log_var_layer(self.encoder(x))))), self.mu_output_layer(self.mu_layer(self.encoder(x))), self.log_var_output_layer(self.log_var_layer(self.encoder(x)))
