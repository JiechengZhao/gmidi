\version "2.23.6"

\header {
  title = "Mocassin Practice"
  composer = "Practice"
}

\score {
  \new PianoStaff <<
    \new Staff = "right" \with {
      instrumentName = "Right Hand"
    } \relative c' {
      \clef "treble"
      \time 4/4
      \tempo 4 = 80
      c4 c4 c4 c4 |
      s1 |
      c4 c4 c4 c4 |
      s1 |
      c4 c4 c4 c4 |
      s1 |
      c4 c4 c4 c4 |
      s1 |
    }
    \new Staff = "left" \with {
      instrumentName = "Left Hand"
    } \relative c {
      \clef "bass"
      \time 4/4
      s1 |
      c4 c4 c4 c4 |
      s1 |
      c4 c4 c4 c4 |
      s1 |
      c4 c4 c4 c4 |
      s1 |
      c4 c4 c4 c4 |
    }
  >>
  \layout { }
  \midi { }
}
