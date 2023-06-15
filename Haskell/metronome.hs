metronome :: Int -> Double
metronome len = fromIntegral len / 4

main :: IO ()
main = do
  input <- getLine
  let len = read input :: Int
      rev = metronome len
  putStrLn (show rev)
