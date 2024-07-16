from pytube import YouTube

def baixar_video(url, caminho_destino='.'):
    try:
        # Cria um objeto YouTube a partir da URL fornecida
        yt = YouTube(url)
        
        # Seleciona o stream de maior resolução que contém tanto vídeo quanto áudio
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        # Baixa o vídeo para o caminho especificado
        stream.download(output_path=caminho_destino)
        
        print(f'Vídeo baixado com sucesso: {stream.title}')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

# Exemplo de uso
url_video = 'https://youtu.be/vKLx4Wg3LZI?si=MsGJ2O1sif2WXGNE'
caminho_destino = '/home/diego/Desktop/to_be_you'
baixar_video(url_video, caminho_destino)
