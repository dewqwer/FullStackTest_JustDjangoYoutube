-- View: public.view_web

-- DROP VIEW public.view_web;

CREATE OR REPLACE VIEW public.view_web
 AS
 SELECT tmq."majorID",
    tmq.speed,
    tmq."faculty_facultyID",
    tmq."majorName",
    tmq."graduation_detail_detailID",
    tmq."queueMajor",
    f."facultyID",
    f."facultyName"
   FROM (( SELECT m."majorID",
            t.speed,
            m."faculty_facultyID",
            m."majorName",
            q."graduation_detail_detailID",
            q."queueMajor"
           FROM ((time_major t
             JOIN major m ON ((m."majorID" = t."major_majorID")))
             JOIN "queue_Management" q ON ((q."major_majorID" = m."majorID")))) tmq
     JOIN faculty f ON ((f."facultyID" = tmq."faculty_facultyID")));

ALTER TABLE public.view_web
    OWNER TO myuser;

