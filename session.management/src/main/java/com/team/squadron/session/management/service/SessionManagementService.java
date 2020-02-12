package com.team.squadron.session.management.service;

import com.team.squadron.session.management.models.TransactionStatus;
import com.team.squadron.session.management.models.UserLog;
import com.team.squadron.session.management.repositories.UserLogRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class SessionManagementService {

    @Autowired
    UserLogRepository userLogRepository;

    public List<UserLog> retrieveUserLogs(String userId) {
        return userLogRepository.findByUserId(userId);
    }

    public boolean createUserSession(UserLog userLog) {
        UserLog createdLog = userLogRepository.insert(userLog);
        if(createdLog != null){
            return true;
        }
        return false;
    }

    public boolean isUserLogExists(String requestId) {
        return userLogRepository.existsById(requestId);
    }

    public boolean updateUserLogs(UserLog userLog) {
        UserLog created = userLogRepository.save(userLog);
        if(created != null){
            return true;
        }
        return false;
    }

    public UserLog getTransactionStatus(String transactionId) {
        return userLogRepository.findById(transactionId).get();
    }
}
