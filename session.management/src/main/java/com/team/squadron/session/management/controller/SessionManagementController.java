package com.team.squadron.session.management.controller;

import com.team.squadron.session.management.models.UserLog;
import com.team.squadron.session.management.service.SessionManagementService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class SessionManagementController {


    SessionManagementService service;

    @RequestMapping(value = "api/v1/session/user/{userId}", method = RequestMethod.GET)
    public @ResponseBody
    List<UserLog> getUserSession(@PathVariable String userId) {
        return  service.retrieveUserLogs(userId);
    }
}
