#存放要刷入所有库的脚本；脚本中不能使用“;”




ALTER TABLE t_promotion_extend
  ADD time_type INT NOT NULL DEFAULT 2 COMMENT '时间类型：@Enum(1,fix,固定时间；2,relativity,相对时间；3,rule_time,活动时间)',
  ADD relativity_begin INT NOT NULL DEFAULT 0 COMMENT '相对于当天的开始时间，0表示今天，1表示第二天(相当于有效期2天)，类推。@Valid(0,10000)',
  ADD relativity_end INT NOT NULL DEFAULT 0 COMMENT '相对于当天的结束时间，0表示今天，1表示第二天，类推。@Valid(0,10000)';

ALTER TABLE t_promotion_extend_log
  ADD time_type INT NOT NULL DEFAULT 2 COMMENT '时间类型：@Enum(1,fix,固定时间；2,relativity,相对时间；3,rule_time,活动时间)',
  ADD relativity_begin INT NOT NULL DEFAULT 0 COMMENT '相对于当天的开始时间，0表示今天，1表示第二天(相当于有效期2天)，类推。@Valid(0,10000)',
  ADD relativity_end INT NOT NULL DEFAULT 0 COMMENT '相对于当天的结束时间，0表示今天，1表示第二天，类推。@Valid(0,10000)';
