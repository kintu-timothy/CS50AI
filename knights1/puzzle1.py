from logic1 import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # Implication(AKnight, And(AKnave, AKnight))
    Or(Not(AKnight), And(AKnave, AKnight))

    # TODO
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Not(Implication(AKnave, And(BKnave, AKnave))),
    Or(BKnave, BKnight),
    Not(And(BKnight, BKnave))
    # TODO
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnave, BKnight),
    Not(And(BKnight, BKnave)),

    # Implication(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))),
    Or(Not(Or(And(AKnight, BKnight), And(AKnave, BKnave))), AKnave ),
    Or(Not(Or(And(AKnight,BKnave), And(BKnight, AKnave))), BKnight)
    # Or(Or(Not(AKnight), And(AKnight, BKnight)), Or(Not(AKnave)), Or(And(AKnave, BKnave), And(AKnight, BKnight))),
    #Or(Not(BKnight), And(BKnight, AKnave)),
    # Or(Or(Not(BKnight), And(BKnight, AKnave)), Or(Not(BKnave), Or(And(BKnave, AKnight), And(BKnight, AKnave))))
    # Not(Implication(BKnave, Or(And(BKnight, AKnave), And(BKnave, AKnight))))
    # TODO
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Or(AKnight, AKnave), 
    # Not(Implication(BKnave, Implication(AKnight, BKnave))),
    # Implication(BKnight, CKnave),
    # Implication(CKnight, AKnight)
    # Or(Implication(AKnight, AKnight),Implication(AKnave, Not(Or(AKnave, AKnight)))),
    # Implication(Implication(BKnave, AKnight), BKnight),
    # Implication(CKnave, BKnight),
    # Implication(Not(CKnave), BKnave),
    # Implication(CKnight, AKnight),
    # Not(Implication(CKnave, Not(AKnight))),
    # Or(CKnight, CKnave),
    # Not(And(CKnave, CKnight))
    Or(Not(AKnight), AKnight),
    # Or(Not(Implication(AKnave, AKnave)), Implication(AKnave, AKnight)),
    # Implication(BKnight, Not(Implication(AKnight, AKnave))), Implication(Or(AKnight, AKnave), AKnave)
    Or(Not(Or(AKnight, AKnave)),AKnave),
    Or(Or(Not(BKnight), Or(Not(AKnave), AKnave))),
    #Not(Or(Implication(BKnight, Or(Implication(AKnight, AKnave), Not(Implication(AKnave, AKnave)))), 
        #Not(Implication(BKnave, Or(Implication(AKnight, BKnave), Not(Implication(AKnave, BKnave))))))),
    #Implication(BKnight, CKnave)
    Or(Not(BKnight), CKnave),
    #Implication(CKnight, AKnight),
    Or(Not(CKnight), AKnight)
    #Or(Implication(BKnight, CKnave), Not(Implication(BKnave, CKnave))),
    #Or(Implication(CKnight, AKnight), Implication(CKnave, AKnight))

    

    # TODO
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
