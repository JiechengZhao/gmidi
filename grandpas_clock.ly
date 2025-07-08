\version "2.23.6"

\header {
  title = "Grandpa's Clock"
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
      c2 c2 |
      s2 s2 |
      c2 c2 |
      s2 s2 |
    }
    \new Staff = "left" \with {
      instrumentName = "Left Hand"
    } \relative c' {
      \clef "bass"
      \time 4/4
      s2 s2 |
      c2 c2 |
      s2 s2 |
      c2 c2 |
    }
  >>
  \layout { }
  \midi { }
}
