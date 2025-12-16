package com.elainehello.loginsystem.service.auth;

import org.springframework.stereotype.Service;
import java.util.UUID;

@Service
public class SessionService {
    
    private static final long TOKEN_EXPIRY_SECONDS = 3600L;

    /**
     * Create Mock fake token for a given userId
     * Later, replace with JWT or session management logic.
     */
    public String createAccessToken(String userId) {
        // for now, returning concatenation of userId and UUID
        return userId + "-" + UUID.randomUUID().toString();
    }

    /**
     * Returns the token expiration time in seconds
     * Currently stubbed to 1 hour (3600 seconds)
     */
    public long getExpireIn() {
        return TOKEN_EXPIRY_SECONDS;
    }
}
