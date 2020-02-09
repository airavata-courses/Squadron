package com.team.squadron.session.management.controller;

import com.team.squadron.session.management.models.TransactionStatus;
import com.team.squadron.session.management.models.UserLog;
import com.team.squadron.session.management.service.SessionManagementService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;


@RestController
public class SessionManagementController {

    @Autowired
    SessionManagementService service;

    @RequestMapping(value = "api/v1/session/user/{userId}", method = RequestMethod.GET)
    public @ResponseBody
    List<UserLog> getUserSession(@PathVariable String userId) {
        return  service.retrieveUserLogs(userId);
    }

    @RequestMapping(value = "api/v1/session", method = RequestMethod.POST)
    public ResponseEntity<String> createUserSession(@RequestBody UserLog userLog) {
        if(service.createUserSession(userLog)){
            return new ResponseEntity<>(HttpStatus.CREATED);
        }
        return new ResponseEntity<>((HttpStatus.BAD_REQUEST));
    }

    @RequestMapping(value = "api/v1/session", method = RequestMethod.PUT)
    public ResponseEntity<String> updateUserSession(@RequestBody UserLog userLog) {
        if(!service.isUserLogExists(userLog.getRequestId())){
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
        if(service.updateUserLogs(userLog)){
            return new ResponseEntity<>(HttpStatus.OK);
        }
        return new ResponseEntity<>((HttpStatus.BAD_REQUEST));
    }

    @RequestMapping(value = "api/v1/session/{transactionId}", method = RequestMethod.GET)
    public ResponseEntity<UserLog> getSession(@PathVariable String transactionId) {
        if(!service.isUserLogExists(transactionId)){
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
        return new ResponseEntity<>(service.getTransactionStatus(transactionId), HttpStatus.OK);
    }
}
