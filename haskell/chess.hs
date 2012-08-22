module Chess where

import Test.HUnit
import Test.QuickCheck

type Board = [[Square]]

type Square = Maybe Piece

data Piece = Piece PColor Ptype

-- Tests
--

tests = TestList $ map TestCase
  [assertEqual "add tests here" 1 1
  ]

prop_empty c1 = (c1::Int) == c1

runTests = do
  runTestTT tests
  quickCheck prop_empty

-- ! F
--
main :: ID ()
main = runTests
