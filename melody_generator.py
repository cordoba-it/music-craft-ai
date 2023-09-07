import pretty_midi
import openai
import os
import random
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

modes = {
    'major': [2, 2, 1, 2, 2, 2, 1],  # Ionian
    'dorian': [2, 1, 2, 2, 2, 1, 2],
    'phrygian': [1, 2, 2, 2, 1, 2, 2],
    'lydian': [2, 2, 2, 1, 2, 2, 1],
    'mixolydian': [2, 2, 1, 2, 2, 1, 2],
    'minor': [2, 1, 2, 2, 1, 2, 2],  # Aeolian
    'locrian': [1, 2, 2, 1, 2, 2, 2],
}


def get_results():
    # Definir una lista de escalas y modos posibles
    scale_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    mode_list = list(modes.keys())  # ['major', 'minor', 'dorian', 'mixolydian', 'lydian', 'phrygian', 'locrian']

    # Elegir al azar una escala y un modo
    random_scale = random.choice(scale_list)
    random_mode = random.choice(mode_list)

    # Generar una descripción de la melodía usando GPT-4
    prompt = f"Describa una melodía en la escala {random_scale} y el modo {random_mode}."
    description = get_completion(prompt)

    # TODO: Tomar la melodía de ChatGPT
    melody = generate_melody(random_scale, random_mode, None)
    # Devolver la melodía, la escala y el modo, y la descripción
    print("melody::", melody)
    return melody, random_scale, random_mode, description


def _generate_melody(root_note, mode):
    # Create a PrettyMIDI object
    midi_data = pretty_midi.PrettyMIDI()

    # Create an Instrument instance for a Cello instrument
    cello_program = pretty_midi.instrument_name_to_program('Cello')
    cello = pretty_midi.Instrument(program=cello_program)

    # Create a Note instance for C4, starting at 0s and ending at .5s
    note = pretty_midi.Note(velocity=100, pitch=pretty_midi.note_name_to_number('C4'), start=0, end=.5)

    # Add the note to the Instrument object
    cello.notes.append(note)

    # Add the Instrument to the PrettyMIDI object
    midi_data.instruments.append(cello)

    # Write out the MIDI data
    midi_data.write('my_melody.mid')
    return "DoremiFasoLasi"


def generate_melody(root_note, mode, melody):
    # Generar la escala
    scale_notes = generate_scale(root_note, modes[mode])
    # root_note = pretty_midi.note_name_to_number(scale)

    if melody is None:
        # Generar una melodía al azar
        melody = [random.choice(scale_notes) for _ in range(5)]  # Generar 100 notas

    # Crear un objeto PrettyMIDI
    midi_data = pretty_midi.PrettyMIDI()

    # Crear un instrumento (piano)
    piano = pretty_midi.Instrument(program=0)

    # Agregar las notas al piano
    start_time = .0
    for note_number in melody:
        # Crear una nota con la duración y el pitch deseados
        note = pretty_midi.Note(velocity=100, pitch=pretty_midi.note_name_to_number(note_number), start=start_time, end=start_time + .5)

        # Agregar la nota al instrumento
        piano.notes.append(note)

        # Avanzar el tiempo de inicio para la siguiente nota
        start_time += .5

    # Add the Instrument to the PrettyMIDI object
    midi_data.instruments.append(piano)

    # Escribir el archivo MIDI
    midi_data.write('my_melody.mid')

    # Devolver la melodía como una secuencia de notas
    return "-".join(note for note in melody)


def generate_scale(root_note, scale_pattern):
    # Convierte la nota raíz a su representación MIDI
    root_note_midi = pretty_midi.note_name_to_number(root_note + '4')

    # Crea una lista para almacenar las notas de la escala
    scale = [root_note_midi]

    # Genera las notas de la escala sumando el patrón a la nota raíz
    for step in scale_pattern:
        scale.append(scale[-1] + step)

    # Convierte las notas MIDI de vuelta a sus nombres
    scale = [pretty_midi.note_number_to_name(note) for note in scale]

    return scale


def get_completion(prompt, model="gpt-3.5-turbo"):  # model="gpt-4"
    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.6,
    )
    print("prompt:: ", prompt)
    print("response:: ", response)
    return response.choices[0].message["content"]
