package com.team.squadron.session.management.service;

import com.team.squadron.session.management.models.UserLog;
import com.team.squadron.session.management.repositories.UserLogRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Service
public class SessionManagementService {

    @Autowired
    UserLogRepository userLogRepository;

    public @ResponseBody List<UserLog> retrieveUserLogs(String userId) {
        return userLogRepository.findByUserId(userId);
    }
}
