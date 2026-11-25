from bot import found_in, recall, forget

def test_found_in():
    assert found_in("אתמול הייתי בחיפה", "חיפה") == True
    assert found_in("אתמול הייתי לחיפה", "חיפה") == True
    assert found_in("טליה היא שחיפה", "חיפה") == False
    assert found_in("אתמול הייתי בחיפה.", "חיפה") == True
    assert found_in("אתמול הייתי בחיפה.", "חיפה.") == True
    assert found_in("אני בבית .", "פיצה") == False
    assert found_in("אני אוהב לאכול", "משה") == False

def test_recall():
    my_memories = [
        {"text": "אתמול הייתי בחיפה", "time": "2026-11-01 10:00"},
        {"text": "מחר נוסעים לחיפה", "time": "2026-11-02 11:00"},
        {"text": "אתמול אכלתי פיצה", "time": "2026-11-03 12:00"},
    ]

    results = recall(my_memories, "אתמול חיפה")
    assert len(results) == 1
    assert results[0]["text"] == "אתמול הייתי בחיפה"

    results = recall(my_memories, "חיפה")
    assert len(results) == 2
    assert results[0]["text"] == "אתמול הייתי בחיפה"
    assert results[1]["text"] == "מחר נוסעים לחיפה"

    results = recall(my_memories, "אתמול")
    assert len(results) == 2
    assert results[0]["text"] == "אתמול הייתי בחיפה"
    assert results[1]["text"] == "אתמול אכלתי פיצה"

    results = recall(my_memories, "תל אביב")
    assert len(results) == 0

def test_forget():
    my_memories = [
        {"text": "mor", "time": "2026-11-09 16:08"},
        {"text": "tom", "time": "2026-11-09 13:47"},
        {"text": "ori", "time": "2026-11-12 12:48"},
    ]

    message = forget(my_memories, "2")
    assert message == "forgotten"
    assert len(my_memories) == 2
    assert my_memories[1]["text"] == "ori"

    message = forget(my_memories, "0")
    assert message == "number doesnt exist"
    assert len(my_memories) == 2

    message = forget(my_memories, "5")
    assert message == "number doesnt exist"
    assert len(my_memories) == 2

    message = forget(my_memories, "abc")
    assert message == "please select number from the list"
    assert len(my_memories) == 2