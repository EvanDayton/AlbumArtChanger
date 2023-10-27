import os
from tkinter import filedialog, Tk
from mutagen.id3 import ID3, APIC

def set_album_art(folder_path, image_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.mp3', '.flac', '.ogg', '.wav')):  # Process supported audio file types
                audio_file_path = os.path.join(root, file)

                try:
                    # Create a new ID3 tag
                    audio = ID3()

                    # Add the album art
                    with open(image_path, "rb") as img_file:
                        image_data = img_file.read()
                    audio["APIC"] = APIC(3, 'image/jpeg', 3, 'Front cover', image_data)

                    # Save the new ID3 tag to the audio file, overwriting any existing tags
                    audio.save(audio_file_path)
                    print(f"Album art set for {audio_file_path}")

                except Exception as e:
                    print(f"Error processing {audio_file_path}: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    root.withdraw()  # Hide the main window

    folder_path = filedialog.askdirectory(title="Select the folder containing audio files to set album art")
    image_path = filedialog.askopenfilename(title="Select the image file for album art")

    if folder_path and image_path:
        set_album_art(folder_path, image_path)
        print("Album art set for audio files.")
    else:
        print("Operation canceled or no folder/image selected.")
