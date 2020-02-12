package com.team.squadron.session.management.repositories;

import com.team.squadron.session.management.models.UserLog;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;

public interface UserLogRepository extends MongoRepository<UserLog, String> {

    List<UserLog> findByUserId(String userId);
}
