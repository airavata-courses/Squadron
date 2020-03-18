import com.team.squadron.session.management.ServerApplication;
import com.team.squadron.session.management.models.TransactionStatus;
import com.team.squadron.session.management.models.UserLog;
import com.team.squadron.session.management.repositories.UserLogRepository;
import com.team.squadron.session.management.service.SessionManagementService;
import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mockito;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;


public class SessionServiceTest {
    private UserLogRepository userLogRepository = Mockito.mock(UserLogRepository.class);
    private SessionManagementService sessionManagementService = new SessionManagementService(userLogRepository);

    @Test
    public void createUserSession(){
        UserLog testLog = new UserLog();
        Mockito.when(userLogRepository.insert(testLog)).thenReturn(testLog);
        boolean created = sessionManagementService.createUserSession(testLog);
        Assert.assertTrue(created);
    }

    @Test
    public void retrieveUserLogsTest(){
        List<UserLog> userLogList = new ArrayList<>();
        userLogList.add(new UserLog());
        Mockito.when(userLogRepository.findByUsername("test-user")).thenReturn(userLogList);
        List<UserLog> result = sessionManagementService.retrieveUserLogs("test-user");
        Assert.assertNotNull(result);
    }

    @Test
    public void updateUserLogsTest(){
        UserLog testLog = new UserLog();
        Mockito.when(userLogRepository.save(testLog)).thenReturn(testLog);
        boolean created = sessionManagementService.updateUserLogs(testLog);
        Assert.assertTrue(created);
    }

    @Test
    public void getUserLogsStatusTest(){
        UserLog userLog = new UserLog();
        userLog.setStatus(TransactionStatus.COMPLETED);
        userLog.setRequest_id("test-user");
        Optional<UserLog> userLogList = Optional.of(userLog);
        Mockito.when(userLogRepository.findById("test-user")).thenReturn(userLogList);
        UserLog result = sessionManagementService.getTransactionStatus("test-user");
        Assert.assertEquals(userLog.getStatus(), result.getStatus());
    }
}
