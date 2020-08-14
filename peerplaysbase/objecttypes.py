ts = [
    "null",
    "base",
    "account",
    "asset",
    "force_settlement",
    "committee_member",
    "witness",
    "limit_order",
    "call_order",
    "custom",
    "proposal",
    "operation_history",
    "withdraw_permission",
    "vesting_balance",
    "worker",
    "balance",
    "tournament",
    "tournament_details",
    "match",
    "game",
    "sport",
    "event_group",
    "event",
    "betting_market_rules",
    "betting_market_group",
    "betting_market",
    "bet",
    "custom_permission",
    "custom_account_authority",
]

object_type = {k: ts.index(k) for k in ts}
