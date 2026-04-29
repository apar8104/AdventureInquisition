story = {
    "start":{
        "text": "you wake up in  dark forest.",
        "choices": [("go left", "left"), ("go right", "right")]
    },
    "left":{
        "text": "you find a cave.",
        "choices": [("enter the cave", "enter"), ("run away", "run")]
    },
    "right":{
        "text": "you reach a river",
        "choices": [("swim across", "swim"), ("follow the river", "follow")]
    },
    "enter":{
        "text": "you found the treasure!",
        "ending": True
    },
    "run":{
        "text": "you are now lost in the forest.",
        "ending": True
    },
    "swim":{
        "text": "i guess the river was wider than it seemed. you have drowned.",
        "ending": True
    },
    "follow":{
        "text": "you have found a village",
        "ending": True
    },
}