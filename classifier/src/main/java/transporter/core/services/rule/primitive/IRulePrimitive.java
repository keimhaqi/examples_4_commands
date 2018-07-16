package transporter.core.services.rule.primitive;

import java.util.Map;

public interface IRulePrimitive {
    boolean action(Map<String, Object> obj);
    boolean action(String obj);
}
