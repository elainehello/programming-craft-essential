package com.elainehello.loginsystem.service.auth;

import com.elainehello.loginsystem.api.auth.LoginResponse;
import com.elainehello.loginsystem.entity.User;
import com.elainehello.loginsystem.repository.UserRepository;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class LoginService {
    private final SessionService sessionService;
    private final UserRepository userRepository;;
    private final PasswordEncoder passwordEncoder;

    // constructor initialize the attributes
    public LoginService(SessionService sessionService,
                        UserRepository userRepository,
                        PasswordEncoder passwordEncoder) {
        this.sessionService = sessionService;
        this.userRepository = userRepository;
        this.passwordEncoder= passwordEncoder;
    }

    public LoginResponse login(String email, String password) {
        User user = userRepository.findByEmail(email)
                .orElseThrow(() -> new RuntimeException("User not found with email: " + email));

        if (!passwordEncoder.matches(password, user.getPasswordHash())) {
            throw new RuntimeException("Invalid password");
        }
        String token = sessionService.createAccessToken(Long.toString(user.getId()));
        long expiresIn = sessionService.getExpireIn();

        return new LoginResponse(token, expiresIn);
    }
}
