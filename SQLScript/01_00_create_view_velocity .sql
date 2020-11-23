-- View: public.view_velocity

-- DROP VIEW public.view_velocity;

CREATE OR REPLACE VIEW public.view_velocity
 AS
 SELECT tmq."majorID",
    tmq."queueMajor",
    tmq."typeDegree",
    tmq."majorName",
    tmq."timeStart",
    tmq."timeStop",
    tmq."requireMeanTime",
    tmq.speed,
    tmq."faculty_facultyID",
    tmq."graduation_detail_detailID",
    f."facultyID",
    f."facultyName"
   FROM ( SELECT m."majorID",
            q."queueMajor",
            m."typeDegree",
            m."majorName",
            t."timeStart",
            t."timeStop",
            t."requireMeanTime",
            t.speed,
            m."faculty_facultyID",
            q."graduation_detail_detailID"
           FROM time_major t
             JOIN major m ON m."majorID" = t."major_majorID"
             JOIN "queue_Management" q ON q."major_majorID" = m."majorID") tmq
     JOIN faculty f ON f."facultyID" = tmq."faculty_facultyID";

ALTER TABLE public.view_velocity
    OWNER TO myuser;

