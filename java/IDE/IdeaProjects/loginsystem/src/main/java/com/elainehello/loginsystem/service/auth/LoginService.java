package com.elainehello.loginsystem.service.auth;

import com.elainehello.loginsystem.api.auth.LoginResponse;
import org.springframework.stereotype.Service;

@Service
public class LoginService {
    private final SessionService sessionService;

    // constructor initialize the attributes
    public LoginService(SessionService sessionService) {
        this.sessionService = sessionService;
    }

    public LoginResponse login(String email, String password) {
        String userId = "user-123";

        String token = sessionService.createAccessToken(userId);
        long expiresIn = sessionService.getExpireIn();

        return new LoginResponse(token, expiresIn);
    }
}
