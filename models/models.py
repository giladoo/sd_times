# -*- coding: utf-8 -*-
import json

from odoo import models, fields, api, Command, _
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError

class SdTimesRecords(models.Model):
    _name = "sd_times.records"
    _description = "Keep your task time"

    name = fields.Char(required=True)
    employee_id = fields.Many2one("hr.employee", default=lambda self: self.env.user.employee_id.id,  required=True)
    department_id = fields.Many2one(related='employee_id.department_id')
    start_time = fields.Datetime(required=True)
    end_time = fields.Datetime(required=True)
    duration = fields.Float(compute="compute_duration", store=True)
    project = fields.Many2one("sd_projects.projects")
    job_type = fields.Many2one('sd_times.job_type')
    location = fields.Many2one('sd_times.location')

    def compute_duration(self):
        for rec in self:
            delta = rec.end_time - rec.start_time
            rec.duration = delta.total_seconds() / 3600
            # total_seconds = int(delta.total_seconds())
            # hours = total_seconds // 3600
            # minutes = (total_seconds % 3600) // 60
            # formatted = f"{hours:02d}:{minutes:02d}"


    def unlink(self):
        ALLOWED_DELETE_DAYS = 3
        # print(f"\n>>>>>>>>>>>>>>>>>\n {self} {datetime.now() - self.create_date}")
        is_operator = self.env.user._has_group("sd_times.group_operators")
        is_old_record = (datetime.now() - self.create_date) > timedelta(days=ALLOWED_DELETE_DAYS)
        if   not is_operator:
            raise ValidationError(_("You are not allowed to remove records older than 3 days "))
        return super().unlink()


class SdTimesJobType(models.Model):
    _name = "sd_times.job_type"
    _description = "Job Type"

    name = fields.Char(required=True)


class SdTimesLocation(models.Model):
    _name = "sd_times.location"
    _description = "Location"

    name = fields.Char(required=True)
