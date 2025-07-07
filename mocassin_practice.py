from midiutil import MIDIFile

# 创建一个新的MIDI文件
# 我们将使用一个轨道，并通过通道区分左右手
midi = MIDIFile(1)
track = 0
time = 0    # 以拍为单位的起始时间
tempo = 108 # BPM (每分钟108拍) - 根据您的要求设定为108
volume = 100 # 音量 (0-127)

# 为左右手定义不同的MIDI通道
channel_right_hand = 0 # 右手通道
channel_left_hand = 1  # 左手通道

midi.addTempo(track, time, tempo)

# 定义音符参数
pitch_c4 = 60 # C4 的MIDI音高值 (中央C)
duration_quarter_note = 1 # 四分音符持续1拍

# 定义一个“两小节单元”的函数：
# 第一小节：右手 4 个四分音符 C4
# 第二小节：左手 4 个四分音符 C4
def add_two_measure_unit(midi_file, current_time, track_num, rh_channel, lh_channel, note_pitch, note_duration, note_volume):
    # 第 1 小节 (4/4拍): 右手 4 个四分音符 C4
    for _ in range(4): # 4个四分音符
        midi_file.addNote(track_num, rh_channel, note_pitch, current_time, note_duration, note_volume)
        current_time += note_duration

    # 第 2 小节 (4/4拍): 左手 4 个四分音符 C4
    for _ in range(4): # 4个四分音符
        midi_file.addNote(track_num, lh_channel, note_pitch, current_time, note_duration, note_volume)
        current_time += note_duration

    return current_time # 返回更新后的时间

# 为了实现“8个小节”，我们需要重复“两小节单元” 4 次。
# 总拍数将是：8 小节 * 4 拍/小节 = 32 拍。
num_repeats_of_two_measure_unit = 4

print("正在生成 MIDI 文件...")
for i in range(num_repeats_of_two_measure_unit):
    print(f"Adding two-measure unit {i+1} of {num_repeats_of_two_measure_unit}...")
    time = add_two_measure_unit(midi, time, track, channel_right_hand, channel_left_hand,
                                  pitch_c4, duration_quarter_note, volume)

# 将MIDI文件写入到磁盘
with open("out/mocassin_practice_8.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("\nMIDI文件 'mocassin_practice_8.mid' 已成功生成！")
print("它现在包含 8 个小节 (32 拍)，BPM 为 108。")