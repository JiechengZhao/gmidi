from midiutil import MIDIFile

# 创建一个新的MIDI文件
# 2个轨道 (track)，我们可以用不同的轨道来代表不同的乐器声部或逻辑上的分离
# 或者，更常见的是，使用同一个轨道，但不同的通道
midi = MIDIFile(1) # 依然使用1个轨道，但会用不同的通道
track = 0
time = 0    # 以拍为单位的起始时间
tempo = 110 # BPM (每分钟110拍)
volume = 100 # 音量 (0-127)

# 为左右手定义不同的通道
channel_right_hand = 0 # 右手通常使用通道 0 (或 1)
channel_left_hand = 1  # 左手通常使用通道 1 (或 2)

midi.addTempo(track, time, tempo)

# 定义音符参数
pitch_c4 = 60 # C4 的MIDI音高值 (中央C)
duration_half_note = 2 # 二分音符持续2拍 (2拍/小节)

# --- 第 1 小节 ---
# 右手 C4 (第一个二分音符)
# 使用 channel_right_hand
midi.addNote(track, channel_right_hand, pitch_c4, time, duration_half_note, volume)
time += duration_half_note

# 右手 C4 (第二个二分音符)
# 使用 channel_right_hand
midi.addNote(track, channel_right_hand, pitch_c4, time, duration_half_note, volume)
time += duration_half_note # 小节结束，时间推进

# --- 第 2 小节 ---
# 左手 C4 (第一个二分音符)
# 使用 channel_left_hand
midi.addNote(track, channel_left_hand, pitch_c4, time, duration_half_note, volume)
time += duration_half_note

# 左手 C4 (第二个二分音符)
# 使用 channel_left_hand
midi.addNote(track, channel_left_hand, pitch_c4, time, duration_half_note, volume)
time += duration_half_note # 小节结束，时间推进

# --- 第 3 小节 (重复第 1 小节) ---
# 右手 C4 (第一个二分音符)
# 使用 channel_right_hand
midi.addNote(track, channel_right_hand, pitch_c4, time, duration_half_note, volume)
time += duration_half_note

# 右手 C4 (第二个二分音符)
# 使用 channel_right_hand
midi.addNote(track, channel_right_hand, pitch_c4, time, duration_half_note, volume)
time += duration_half_note # 小节结束，时间推进

# --- 第 4 小节 (重复第 2 小节) ---
# 左手 C4 (第一个二分音符)
# 使用 channel_left_hand
midi.addNote(track, channel_left_hand, pitch_c4, time, duration_half_note, volume)
time += duration_half_note

# 左手 C4 (第二个二分音符)
# 使用 channel_left_hand
midi.addNote(track, channel_left_hand, pitch_c4, time, duration_half_note, volume)
# time += duration_half_note # 最后一个音符，不需要再推进时间

# 将MIDI文件写入到磁盘
with open("grandpas_clock_4_measures_hands.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("MIDI文件 'grandpas_clock_4_measures_hands.mid' 已成功生成！")
print("它包含四个小节，后两个小节重复前两个，并区分了左右手通道。")
