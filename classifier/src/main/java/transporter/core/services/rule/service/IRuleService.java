package transporter.core.services.rule.service;

import java.util.Map;

public interface IRuleService {
    boolean classifier(Map<String, Object> obj);
    boolean classifier(String obj);
}
