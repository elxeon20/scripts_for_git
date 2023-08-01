import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

def download_video(url):
    try:
        youtube = YouTube(url)
        video_stream = youtube.streams.filter(file_extension="mp4").first()
        video_filename = video_stream.download()
        return video_filename
    except Exception as e:
        print("Произошла ошибка при скачивании видео:", str(e))
        return None

def cut_and_convert_to_mp3(input_file, start_time, end_time, output_file):
    try:
        video_clip = VideoFileClip(input_file).subclip(start_time, end_time)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_file, codec='mp3')
        audio_clip.close()
        video_clip.close()
    except Exception as e:
        print(f"Произошла ошибка при обработке видео {output_file}: {str(e)}")

# Ссылка на видео с YouTube
video_url = "https://www.youtube.com/watch?v=jmQ0HUs8kic"

# Таймкоды и наименования частей для разделения
timecodes = [
    (0, 204, "On The Floor"),
    (204, 462, "Set Fire to the Rain"),
    (462, 701, "Faded"),
    (701, 898, "Unholy"),
    (898, 1019, "Save Your Tears"),
    (1019, 1384, "We Don_t Talk Anymore"),
    (1384, 1572, "THAT GIRL"),
    (1572, 1791, "Beautiful Girls"),
    (1791, 1961, "I'm Good (Blue)"),
    (1961, 2178, "Made You Look"),
    (2178, 2428, "Apologize"),
    (2428, 2671, "Despacito"),
    (2671, 2900, "Diamonds"),
    (2900, 3123, "Dusk Till Dawn"),
    (3123, 3371, "Lambada"),
    (3371, 3597, "Timber"),
    (3597, 3813, "Attention"),
    (3813, 4042, "The Drum"),
    (4042, 4223, "Zombie"),
    (4223, 4456, "Wake me up"),
    (4456, 4659, "The Spectre"),
    (4659, 4888, "Heroes"),
    (4888, 5094, "Lean On - Major Lazer"),
    (5094, 5171, "Reality")
]


# Скачиваем видео 1 раз
video_filename = download_video(video_url)

if video_filename:
    for idx, (start_time, end_time, name) in enumerate(timecodes):
        output_file_mp3 = f"{name}.mp3"
        cut_and_convert_to_mp3(video_filename, start_time, end_time, output_file_mp3)
        print(f"{idx + 1}/{len(timecodes)}: Сохранено {output_file_mp3}")

    # Удаляем исходный видеофайл
    os.remove(video_filename)

print("Готово!")
