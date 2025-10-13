from PIL import Image

# Caminho original da imagem
caminho_original = './asset/Enemy.png'

# Caminho para salvar a imagem corrigida
caminho_corrigido = './asset/Enemy.png'  # Sobrescreve o original

try:
    # Abre a imagem
    img = Image.open(caminho_original)

    # Remove o perfil ICC (se houver)
    icc_profile = img.info.get('icc_profile', None)

    if icc_profile:
        img.save(caminho_corrigido, format='PNG', icc_profile=None)
        print("✅ Imagem corrigida: perfil ICC removido.")
    else:
        img.save(caminho_corrigido, format='PNG')
        print("⚠️ Imagem não tinha perfil ICC, mas foi salva novamente.")

except Exception as e:
    print(f"❌ Erro ao processar a imagem: {e}")