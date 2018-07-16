package transporter.core.model.rule;

import java.util.Map;

public interface IRule {
    boolean check(Map<String, Object> obj);
}
