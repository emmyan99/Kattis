{-
jackolanternjuxtaposition :: Int -> Int -> Int -> Int
jackolanternjuxtaposition x y z = x*y*z

main :: IO ()
main = do
  inputX <- getLine
  inputY <- getLine
  inputZ <- getLine
  let x = read inputX :: Int
  let y = read inputY :: Int
  let z = read inputZ :: Int
      ans = jackolanternjuxtaposition x y z
  putStrLn (show ans)
  -}

jackolanternjuxtaposition :: Int -> Int -> Int -> Int
jackolanternjuxtaposition x y z = x*y*z

main :: IO ()
main = do
  input <- getLine
  let [x, y, z] = map read (words input) :: [Int]
    -- words converts input to a list
    -- map read applies read to each element in list, converting x y and z to ints
      ans = jackolanternjuxtaposition x y z
  putStrLn (show ans)