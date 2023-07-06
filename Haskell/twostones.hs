twostones :: Int -> String
twostones stones
  | mod stones 2 == 0 = "Bob"
  | otherwise = "Alice"

main :: IO ()
main = do
  input <- getLine
  let stones = read input :: Int
      winner = twostones stones
  putStrLn winner
