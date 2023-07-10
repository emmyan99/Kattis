import Data.List (delete)
import Data.List (isPrefixOf)

readLines :: Int -> [String] -> [String]
readLines n lines = do
    line <- getLine
    readLines (n - 1) (line : lines)

isExit :: String -> [String] -> Bool
isExit line = "exit " `isPrefixOf` line

isEntry :: String -> [String] -> Bool
isEntry line = "entry " `isPrefixOf` line

checkBuilding :: String -> [String] -> Bool
checkBuilding name building = name `elem` building

extractName :: String -> String
extractName line
  | isExit line = delete "exit " line
  | isEntry line = delete "entry " line


securityProcess :: [String] -> [String] -> [String]
securityProcess line building
    | not(checkBuilding extractName line building) && isEntry line = -- add extractName line  ++ "entered." to output and add extraName line in building 
        let output = extractName line ++ " entered."
            building = extractName line : building
    | (checkBuilding extractName line building) && isExit line = -- add extractName line  ++ "exited." to output and remove extraName line from building 
        let output = extractName line ++ " exited."
            building = delete (extractName line)  building
    | (checkBuilding extractName line building) && isEntry line = -- add extractName line  ++ "entered. (ANOMALY)" to output
        let output = extractName line ++ " entered. (ANOMALY)"
    | not(checkBuilding extractName line building) && isExit line = -- add extractName line  ++ "exited. (ANOMALY)" to output
        let output = extractName line ++ " exited. (ANOMALY)"


processLines :: [String] -> [String] -> [String]
processLines [] _ = [] -- Base case: empty list of lines
processLines (line : rest) building =
  let (updatedBuilding, output) = securityProcess line building
  in output : processLines rest updatedBuilding


main :: IO ()
main = do
    input <- getLine
    let x = read input :: Int
    lines <- readLines x [] -- lines ["entry Abbey", "entry Abbey", "exit Abbey"]

    let building = []

    let output = processLines lines building
    mapM_ putStrLn output
