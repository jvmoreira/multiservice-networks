import React, { FormEvent, Fragment, FunctionComponent, ReactElement, useCallback } from 'react';
import { NfvTeCategory, NfvTeFunction, useNfvTeValue } from '@/commons/nfv-te-values';
import { CategoryField } from './fields/category-field';
import { FunctionNameField } from './fields/function-name-field';
import { ClientInterfaceField } from './fields/client-interface-field';
import { ServerInterfaceField } from './fields/server-interface-field';
import { TwoRateThreeColorParameters } from './fields/two-rate-three-color-parameters';
import { TokenBucketPolicerParameters } from './fields/token-bucket-policer-parameters';
import { SingleRateThreeColorParameters } from './fields/single-rate-three-color-parameters';
import { TokenBucketShaperParameters } from './fields/token-bucket-shaper-parameters';
import { LeakyBucketParameters } from './fields/leaky-bucket-parameters';
import { DebugField } from './fields/debug-field';

export function Form(): ReactElement {
  const [category] = useNfvTeValue('category');
  const [functionName] = useNfvTeValue('functionName');
  const NfvTeFunctionParametersComponent = resolveNfvTeFunctionParametersComponent(category, functionName);

  const onSubmit = useCallback((evt: FormEvent) => evt.preventDefault(), []);

  return (
    <section id="form-section">
      <form onSubmit={onSubmit} style={{ display: 'flex', flexFlow: 'column' }}>
        <CategoryField />
        <FunctionNameField />

        <NfvTeFunctionParametersComponent />

        <ClientInterfaceField />
        <ServerInterfaceField />
        <DebugField />
      </form>
    </section>
  );
}

function resolveNfvTeFunctionParametersComponent(
  category: NfvTeCategory,
  functionName: NfvTeFunction,
): FunctionComponent {
  switch (category) {
    case NfvTeCategory.UNSELECTED:
      return Fragment;
    case NfvTeCategory.SHAPING:
      return resolveNfvTeShapingFunctionsParametersComponent(functionName);
    case NfvTeCategory.POLICING:
      return resolveNfvTePolicingFunctionsParametersComponent(functionName);
    default:
      throw new Error(`Invalid category: ${category}`);
  }
}

function resolveNfvTeShapingFunctionsParametersComponent(functionName: NfvTeFunction): FunctionComponent {
  switch (functionName) {
    case NfvTeFunction.UNSELECTED:
      return Fragment;
    case NfvTeFunction.LEAKY_BUCKET:
      return LeakyBucketParameters;
    case NfvTeFunction.TOKEN_BUCKET:
      return TokenBucketShaperParameters;
    default:
      throw new Error(`Invalid shaping function name: ${functionName}`);
  }
}

function resolveNfvTePolicingFunctionsParametersComponent(functionName: NfvTeFunction): FunctionComponent {
  switch (functionName) {
    case NfvTeFunction.UNSELECTED:
      return Fragment;
    case NfvTeFunction.TOKEN_BUCKET:
      return TokenBucketPolicerParameters;
    case NfvTeFunction.ONE_RATE_THREE_COLOR:
      return SingleRateThreeColorParameters;
    case NfvTeFunction.TWO_RATE_THREE_COLOR:
      return TwoRateThreeColorParameters;
    default:
      throw new Error(`Invalid policing function name: ${functionName}`);
  }
}
