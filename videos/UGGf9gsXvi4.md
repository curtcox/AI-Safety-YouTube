---
id: "UGGf9gsXvi4"
title: "Sparse autoencoders for efficient learning | Neel Nanda at FAR.AI's alignment workshop"
url: "https://www.youtube.com/watch?v=UGGf9gsXvi4"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-05-12"
duration_seconds: 50
is_short: true
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Sparse autoencoders for efficient learning | Neel Nanda at FAR.AI's alignment workshop

[Watch on YouTube](https://www.youtube.com/watch?v=UGGf9gsXvi4) · FAR․AI · 2025-05-12 · 0:50

## Description

```text
Sparse autoencoders for efficient learning | Neel Nanda at FAR.AI's alignment workshop
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] Sparse autoenccoders are a technique to both learn this dictionary and learn this sparse vector of coefficients. The key idea is to train a wide autoenccoder to reconstruct the input activations. The hope is that the decoder, just a matrix, is this dictionary of meaningful vectors. That each latent in the autoenccoder is a different concept. And that the activations of these latents on a given input uh tell us the sparse vector of coefficients. And to make it sparse, we train this on a model's activations. And the hope is that if there is an interpretable sparse decomposition that just optimizing something to be sparse without optimizing it to be interpretable, we'll stumble across that interpretable decomposition. And it kind of works.
