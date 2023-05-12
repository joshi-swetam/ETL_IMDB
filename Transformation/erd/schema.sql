-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/AMiICH
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "imdb_top_250" (
    "imdb_title_id" int   NOT NULL,
    "title_id" int   NOT NULL,
    "rank" int   NULL,
    "years_running" varchar(200)   NULL,
    "certificate" varchar(20)   NULL,
    "rating" float   NULL,
    "votes" int   NULL,
    "Synopsis" varchar(1000)   NOT NULL,
    CONSTRAINT "pk_imdb_top_250" PRIMARY KEY (
        "imdb_title_id"
     )
);

CREATE TABLE "title" (
    "title_id" int   NOT NULL,
    "title" varchar(200)   NOT NULL,
    CONSTRAINT "pk_title" PRIMARY KEY (
        "title_id"
     )
);

CREATE TABLE "category" (
    "category_id" int   NOT NULL,
    "category" varchar(100)   NOT NULL,
    CONSTRAINT "pk_category" PRIMARY KEY (
        "category_id"
     )
);

CREATE TABLE "actor" (
    "actor_id" int   NOT NULL,
    "actor" varchar(200)   NOT NULL,
    CONSTRAINT "pk_actor" PRIMARY KEY (
        "actor_id"
     )
);

CREATE TABLE "network" (
    "network_id" int   NOT NULL,
    "network" varchar(20)   NOT NULL,
    CONSTRAINT "pk_network" PRIMARY KEY (
        "network_id"
     )
);

CREATE TABLE "award" (
    "award_id" int   NOT NULL,
    "award" varchar(100)   NOT NULL,
    CONSTRAINT "pk_award" PRIMARY KEY (
        "award_id"
     )
);

-- Table documentation comment 2
CREATE TABLE "title_category" (
    "title_id" int   NOT NULL,
    "category_id" int   NOT NULL,
    CONSTRAINT "pk_title_category" PRIMARY KEY (
        "title_id","category_id"
     )
);

CREATE TABLE "nomination" (
    "nomination_id" int   NOT NULL,
    "award_id" int   NOT NULL,
    "year" int   NOT NULL,
    "title_id" int   NULL,
    "actor_id" int   NULL,
    "network_id" int   NOT NULL,
    "category_id" int   NOT NULL,
    "role" varchar(100)   NULL,
    "episode" varchar(200)   NULL,
    "producers" varchar(1000)   NULL,
    "winner" boolean   NOT NULL,
    CONSTRAINT "pk_nomination" PRIMARY KEY (
        "nomination_id","category_id"
     )
);

ALTER TABLE "imdb_top_250" ADD CONSTRAINT "fk_imdb_top_250_title_id" FOREIGN KEY("title_id")
REFERENCES "title" ("title_id");

ALTER TABLE "title_category" ADD CONSTRAINT "fk_title_category_title_id" FOREIGN KEY("title_id")
REFERENCES "title" ("title_id");

ALTER TABLE "title_category" ADD CONSTRAINT "fk_title_category_category_id" FOREIGN KEY("category_id")
REFERENCES "category" ("category_id");

ALTER TABLE "nomination" ADD CONSTRAINT "fk_nomination_award_id" FOREIGN KEY("award_id")
REFERENCES "award" ("award_id");

ALTER TABLE "nomination" ADD CONSTRAINT "fk_nomination_title_id" FOREIGN KEY("title_id")
REFERENCES "title" ("title_id");

ALTER TABLE "nomination" ADD CONSTRAINT "fk_nomination_actor_id" FOREIGN KEY("actor_id")
REFERENCES "actor" ("actor_id");

ALTER TABLE "nomination" ADD CONSTRAINT "fk_nomination_network_id" FOREIGN KEY("network_id")
REFERENCES "network" ("network_id");

ALTER TABLE "nomination" ADD CONSTRAINT "fk_nomination_category_id" FOREIGN KEY("category_id")
REFERENCES "category" ("category_id");

