from relational_algebra import *
import sqlite3


class Expressions():

    sample_query = Projection(
        NaturalJoin(Selection(Relation("Trainer"), Equals("credentials", "CNS")), Relation("person")), ["name"])


    expression1 = Projection(("person"), ["name","gender"])


    expression2 = Projection(NaturalJoin(NaturalJoin(NaturalJoin(Selection(Relation("non_student"), Equals("member_type", "Faculty")), Relation("member")), Relation("university_affiliate")), Relation("person")) ,["name","department"] )


    expression3 = Projection(ThetaJoin(Union(NaturalJoin(Selection(Relation("space"), Equals("space_description", "cardio room")),
                                          Selection(Relation("location_reading"), Equals("timestamp", "2023-04-01 00:00:00"))),
                              NaturalJoin(Selection(Relation("space"), Equals("space_description", "weight room")),
                                          Selection(Relation("location_reading"), Equals("timestamp", "2023-04-01 00:00:00")))), Relation("person"), Equals("person_id","card_id")),["name"])


    expression4 = Projection(NaturalJoin(Division(Relation("attends"), Projection(Relation("events"), ["event_id"])),Relation("person")),["name"])


    expression5 = Projection(Selection(NaturalJoin(Relation("space"),Relation("events")), GreaterEquals("capacity", "max_capacity")),["event_id"])


    expression6 = Projection(NaturalJoin(Relation("person"),Division(
                    Projection(NaturalJoin(
                    NaturalJoin(Selection(Relation("space"), Equals("space_description", "cardio room")),
                                Selection(Relation("equipment"), Equals("is_available", 0))),
                    Relation("usage_reading")),["card_id","equipment_id"]),
                    Projection(NaturalJoin(
                    NaturalJoin(Selection(Relation("space"), Equals("space_description", "cardio room")),
                                Selection(Relation("equipment"), Equals("is_available", 0))),
                    Relation("usage_reading")),["equipment_id"]))),["name"])
    # expression7 =

    # expression8 =

    # expression9 =

    # expression10 =


    sql_con = sqlite3.connect("sample122A.db")
