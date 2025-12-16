package com.elainehello.loginsystem.api.auth;

import com.elainehello.loginsystem.service.auth.SessionService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1/auth")
public class LogoutController {

    private final SessionService sessionService;

    // initialize property/attribute
    public LogoutController(SessionService sessionService) {
        this.sessionService = sessionService;
    }

    @PostMapping("/logout")
    public ResponseEntity<Void> logout(@RequestHeader("Authorization") String authHeader) {
        try {
            // Extract token from "Bearer <token>"
            String token = authHeader.replace("Bearer ", "");
            sessionService.invalidateToken(token);
            return ResponseEntity.ok().build();
        } catch (Exception e) {
            return ResponseEntity.badRequest().build();
        }
    }
}
