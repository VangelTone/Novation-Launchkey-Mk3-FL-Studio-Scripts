# Main File
# Name=Novation Launchkey49 Mk3
import transport
import midi
import mixer
import general

# Below are the variables which can be changed
play_button = 115
stop_button = 116
record_button = 117
metronome_button = 76
undo_button = 77
loop_button = 118
fader = (71, 72, 73, 74, 75, 76, 77, 78, 79)


# Function starts from below
def OnMidiMsg(transport_controller):
    transport_controller.handled = False
    print(transport_controller.midiId, transport_controller.status, transport_controller.port,
          transport_controller.data1, transport_controller.data2)
    if transport_controller.midiId == midi.MIDI_CONTROLCHANGE:
        if transport_controller.data2 > 0:
            if transport_controller.data1 == play_button:
                print('Start')
                transport.start()
                transport_controller.handled = True
            if transport_controller.data1 == stop_button:
                print('Stop')
                transport.stop()
                transport_controller.handled = True
            if transport_controller.data1 == record_button:
                print('Record')
                transport.record()
                transport_controller.handled = True
            if transport_controller.data1 == loop_button:
                print('Pattern/Song Mode')
                transport.setLoopMode()
            if transport_controller.data1 == undo_button:
                print('Undo')
                general.undo()
                transport_controller.handled = True
            if transport_controller.data1 == fader[0]:
                print('Undo')
                mixer.setTrackVolume(1, transport_controller.data2 / 100)
                transport_controller.handled = True
            if transport_controller.data1 == fader[1]:
                print('Undo')
                mixer.setTrackVolume(2, transport_controller.data2 / 100)
                transport_controller.handled = True
            if transport_controller.data1 == fader[2]:
                print('Undo')
                mixer.setTrackVolume(3, transport_controller.data2 / 100)
                transport_controller.handled = True
            if transport_controller.data1 == fader[3]:
                print('Undo')
                mixer.setTrackVolume(4, transport_controller.data2 / 100)
                transport_controller.handled = True
            if transport_controller.data1 == fader[8]:
                print('Undo')
                mixer.setTrackVolume(0, transport_controller.data2 / 100)
                transport_controller.handled = True
